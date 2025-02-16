// Chargement des derniers fichiers
document.addEventListener('DOMContentLoaded', async () => {
    const res = await fetch('data/latest.json');
    const files = await res.json();
    
    const container = document.querySelector('.file-list');
    
    files.forEach(file => {
        container.innerHTML += `
            <a href="${file.path}" data-type="${file.type}">
                ${file.name}
                <small>${file.date}</small>
            </a>
        `;
    });
});

// Filtre des exams
document.getElementById('yearFilter')?.addEventListener('change', function() {
    const year = this.value;
    document.querySelectorAll('.exam-card').forEach(card => {
        card.hidden = year !== 'all' && !card.dataset.year.includes(year);
    });
});