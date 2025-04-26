document.addEventListener('DOMContentLoaded', function() {
    // Add focus and blur effects for search inputs
    const searchInputs = document.querySelectorAll('.search-input');
    
    searchInputs.forEach(input => {
        // Add focus class to parent container when input is focused
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('active');
        });
        
        // Remove focus class when input loses focus
        input.addEventListener('blur', function() {
            if (this.value === '') {
                this.parentElement.classList.remove('active');
            }
        });
    });
    
    // Add animation for search button
    const searchButton = document.querySelector('.search-button');
    if (searchButton) {
        searchButton.addEventListener('mouseenter', function() {
            this.classList.add('hover');
        });
        
        searchButton.addEventListener('mouseleave', function() {
            this.classList.remove('hover');
        });
    }
}); 

document.querySelectorAll('.close').forEach(btn => {
    btn.onclick = () => window.location.hash = '';
  });