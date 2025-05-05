// Functionality for gestion-annonces.html
document.addEventListener('DOMContentLoaded', function() {
    // Variables pour stocker les images
    let imageFiles = [];
    
    // Sélectionner les éléments DOM
    const imagePreview = document.querySelector('.image-preview');
    const imagePreviewContainer = document.querySelector('.image-preview-container');
    const fileInput = document.querySelector('#images');
    const annonceForm = document.querySelector('#annonceForm');
    const annoncesList = document.querySelector('.annonces-list');
    
    // Charger les annonces existantes au démarrage
    loadAnnonces();
    
    // Gérer le clic sur la zone de prévisualisation des images
    if (imagePreview) {
        imagePreview.addEventListener('click', function() {
            fileInput.click();
        });
    }
    
    // Gérer le changement de fichiers dans l'input
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const files = e.target.files;
            
            if (files.length) {
                Array.from(files).forEach(file => {
                    if (file.type.match('image.*')) {
                        const reader = new FileReader();
                        
                        reader.onload = function(e) {
                            // Ajouter l'image à la liste
                            imageFiles.push({
                                file: file,
                                src: e.target.result
                            });
                            
                            // Mettre à jour la prévisualisation
                            updateImagePreview();
                        };
                        
                        reader.readAsDataURL(file);
                    }
                });
            }
        });
    }
    
    // Fonction pour mettre à jour la prévisualisation des images
    function updateImagePreview() {
        if (imagePreviewContainer) {
            imagePreviewContainer.innerHTML = '';
            
            imageFiles.forEach((image, index) => {
                const previewItem = document.createElement('div');
                previewItem.className = 'preview-item';
                previewItem.innerHTML = `
                    <img src="${image.src}" alt="Image preview">
                    <div class="remove-image" data-index="${index}">
                        <i class="fas fa-times"></i>
                    </div>
                `;
                
                imagePreviewContainer.appendChild(previewItem);
                
                // Gérer la suppression d'une image
                previewItem.querySelector('.remove-image').addEventListener('click', function(e) {
                    e.stopPropagation();
                    const index = parseInt(this.dataset.index);
                    imageFiles.splice(index, 1);
                    updateImagePreview();
                });
            });
        }
    }
    
    
        
        }

); 