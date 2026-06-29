    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        if (!name || !email || !message) {
            alert('Please fill in all fields.');
            return;
        }

        alert('Thank you for your message. We will contact you soon!');
        console.log('Form submitted:', { name, email, message });
        document.getElementById('contactForm').reset();
    });


    document.getElementById('reservationForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const name = document.getElementById('res-name').value;
        const email = document.getElementById('res-email').value;
        const date = document.getElementById('res-date').value;
        const time = document.getElementById('res-time').value;
        const guests = document.getElementById('res-guests').value;

        if (name === "" || email === "") {
            alert('Please enter your name and email');
            return false;
        }

        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(email)) {
            alert('Please enter a valid email address');
            return;
        }

        const today = new Date();
        today.setHours(0, 0, 0, 0);
        const selectedDate = new Date(date);
        selectedDate.setHours(0, 0, 0, 0);

        if (selectedDate < today) {
            alert("Date cannot be in the past.");
            return;
        }

        alert('Thank you for your reservation request. We will confirm shortly!');
        console.log('Reservation submitted:', { name, email, date, time, guests });
        document.getElementById('reservationForm').reset();
    });


    function filterMenu(category) {
        const menuItems = document.querySelectorAll('.menu-item');

        menuItems.forEach(item => {

            const itemCategory = item.getAttribute('data-category');

            if (category === 'all' || itemCategory === category) {
                item.classList.remove('hidden'); // Show item

            } else {
                item.classList.add('hidden');    // Hide item

            }
        });
    }

    document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {

            e.preventDefault();

            const targetId = this.getAttribute('href');

            if (targetId === '#') return;
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth', // Enables smooth scrolling
                    block: 'start'      // Aligns element to the top of the viewport
                });
            }
        });
    });

    // Broken mobile menu toggle functionality
    // Missing mobile menu button and functionality

    //TESTING TODO
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {

            mobileMenu.classList.toggle('hidden');
            const isExpanded = mobileMenu.classList.contains('hidden') ? 'false' : 'true';
            mobileMenuBtn.setAttribute('aria-expanded', isExpanded);

        });

    } else {
        console.error('Mobile menu button or menu element not found in DOM.');
    }
