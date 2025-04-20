// Navbar functionality
document.addEventListener('DOMContentLoaded', function() {
    // Gestion du menu burger
    const burgerMenu = document.querySelector('.burger-menu');
    const navLinks = document.querySelector('.nav-links');

    if (burgerMenu && navLinks) {
        // Initialize properly - set initial state
        if (window.innerWidth <= 1000) {
            navLinks.style.display = 'none';
        } else {
            navLinks.style.display = 'flex';
        }

        // Window resize handler
        window.addEventListener('resize', function() {
            if (window.innerWidth > 1000) {
                navLinks.style.display = 'flex';
                navLinks.classList.remove('active');
                burgerMenu.classList.remove('active');
            } else if (!navLinks.classList.contains('active')) {
                navLinks.style.display = 'none';
            }
        });

        burgerMenu.addEventListener('click', function() {
            this.classList.toggle('active');
            navLinks.classList.toggle('active');
            
            if (navLinks.classList.contains('active')) {
                navLinks.style.display = 'flex';
            } else {
                navLinks.style.display = 'none';
            }
        });

        // Only close menu when clicking on a nav link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 1000) {
                    burgerMenu.classList.remove('active');
                    navLinks.classList.remove('active');
                    navLinks.style.display = 'none';
                }
            });
        });
    }

    // Highlight current page in navbar
    const currentPage = window.location.pathname.split('/').pop();
    const navLinksItems = document.querySelectorAll('.nav-links a');
    
    navLinksItems.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage) {
            link.style.color = '#2563eb';
            link.style.fontWeight = '600';
        }
    });

    // Initialiser le compteur de notifications
    function initNotificationsCount() {
        // Simuler des notifications non lues
        const notificationsData = JSON.parse(localStorage.getItem('notificationsData')) || [];
        const unreadCount = notificationsData.filter(n => !n.read).length || 2; // Default to 2 if no data
        
        const counter = document.querySelector('.notifications-count');
        if (counter) {
            counter.textContent = unreadCount;
            if (unreadCount === 0) {
                counter.style.display = 'none';
            } else {
                counter.style.display = 'inline-block';
            }
        }
    }
    
    // Initialiser le compteur
    initNotificationsCount();
}); 