import os
import requests
from duckduckgo_search import DDGS
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image
from io import BytesIO
import time

def download_image(img_name):
    # Configuration
    search_term = img_name.replace('_', ' ').replace('.jpg', '')
    output_dir = "downloaded_images"
    max_results = 50
    min_width = 400  # Taille minimale en pixels
    min_height = 400
    
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.images(
                search_term, 
                max_results=max_results,
                safesearch='off',
                size='medium',
            )]
            
            for result in results:
                img_url = result['image']
                
                try:
                    # Téléchargement avec timeout
                    response = requests.get(img_url, stream=True, timeout=(5, 10))
                    
                    if response.status_code == 200:
                        # Vérification de la taille de l'image
                        img_data = BytesIO(response.content)
                        with Image.open(img_data) as img:
                            if img.width >= min_width and img.height >= min_height:
                                # Sauvegarde de l'image
                                file_path = os.path.join(output_dir, img_name)
                                with open(file_path, 'wb') as f:
                                    f.write(response.content)
                                print(f"✅ Téléchargé: {img_name}")
                                return True
                            
                except Exception as e:
                    continue  # Passe à l'image suivante en cas d'erreur
                    
    except Exception as e:
        print(f"❌ Erreur pour {img_name}: {str(e)}")
    
    print(f"⚠️ Aucune image valide trouvée pour {img_name}")
    return False

def main():
    image_files = [
        "tartare_thon_avocat.jpg",
        "croissants_maison.jpg"
    ]

    start_time = time.time()
    success_count = 0
    
    # Téléchargement avec suivi de progression
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(download_image, img): img for img in image_files}
        
        for future in as_completed(futures):
            img_name = futures[future]
            try:
                if future.result():
                    success_count += 1
            except Exception as e:
                print(f"❌ Erreur majeure pour {img_name}: {str(e)}")

    # Statistiques
    elapsed_time = time.time() - start_time
    print(f"\n📊 Résultats :")
    print(f"- Images téléchargées : {success_count}/{len(image_files)}")
    print(f"- Temps écoulé : {elapsed_time:.2f} secondes")
    print(f"- Taux de succès : {(success_count/len(image_files))*100:.1f}%")

if __name__ == "__main__":
    main()