document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle) {
      menuToggle.addEventListener('click', function() {
        navLinks.classList.toggle('active');
      });
    }
  
    // Task completion toggle
    const taskCheckboxes = document.querySelectorAll('.task-checkbox');
    
    taskCheckboxes.forEach(checkbox => {
      checkbox.addEventListener('change', function() {
        const taskItem = this.closest('.task-item');
        if (this.checked) {
          taskItem.classList.add('completed');
        } else {
          taskItem.classList.remove('completed');
        }
        updateProgressBars();
      });
    });
  
    // Project creation modal
    const newProjectBtn = document.getElementById('new-project-btn');
    const projectModal = document.getElementById('project-modal');
    const closeModalBtn = document.querySelector('.close-modal');
    
    if (newProjectBtn && projectModal) {
      newProjectBtn.addEventListener('click', function() {
        projectModal.style.display = 'flex';
      });
      
      closeModalBtn.addEventListener('click', function() {
        projectModal.style.display = 'none';
      });
      
      window.addEventListener('click', function(event) {
        if (event.target == projectModal) {
          projectModal.style.display = 'none';
        }
      });
    }
  
    // Update progress bars
    function updateProgressBars() {
      const progressBars = document.querySelectorAll('.progress-bar');
      
      progressBars.forEach(bar => {
        const progressPercentage = Math.floor(Math.random() * 100); // For demo purposes
        const progressFill = bar.querySelector('.progress-fill');
        progressFill.style.width = progressPercentage + '%';
        
        // Update percentage text if it exists
        const percentageText = bar.nextElementSibling?.querySelector('.percentage');
        if (percentageText) {
          percentageText.textContent = progressPercentage + '%';
        }
      });
    }
  
    // Initialize progress bars on load
    updateProgressBars();
  
    // Daily quote rotation (for dashboard)
    const quotes = [
      { text: "The secret of getting ahead is getting started.", author: "Mark Twain" },
      { text: "Don't watch the clock; do what it does. Keep going.", author: "Sam Levenson" },
      { text: "Believe you can and you're halfway there.", author: "Theodore Roosevelt" },
      { text: "It always seems impossible until it's done.", author: "Nelson Mandela" },
      { text: "The future depends on what you do today.", author: "Mahatma Gandhi" }
    ];
  
    const quoteContainer = document.querySelector('.quote-container');
    if (quoteContainer) {
      const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
      quoteContainer.querySelector('.quote-text').textContent = `"${randomQuote.text}"`;
      quoteContainer.querySelector('.quote-author').textContent = `— ${randomQuote.author}`;
    }
  
    // Form validation
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
      form.addEventListener('submit', function(event) {
        let valid = true;
        const requiredInputs = form.querySelectorAll('[required]');
        
        requiredInputs.forEach(input => {
          if (!input.value.trim()) {
            valid = false;
            input.classList.add('invalid');
            
            const errorMessage = input.nextElementSibling?.classList.contains('error-message') ? 
              input.nextElementSibling : document.createElement('span');
            
            if (!input.nextElementSibling?.classList.contains('error-message')) {
              errorMessage.classList.add('error-message');
              errorMessage.textContent = 'This field is required';
              input.parentNode.insertBefore(errorMessage, input.nextSibling);
            }
          } else {
            input.classList.remove('invalid');
            if (input.nextElementSibling?.classList.contains('error-message')) {
              input.nextElementSibling.remove();
            }
          }
        });
        
        if (!valid) {
          event.preventDefault();
        }
      });
    });
  
    // Add animation classes
    const fadeElements = document.querySelectorAll('.fade-in-element');
    fadeElements.forEach((el, index) => {
      el.classList.add('fade-in');
      el.classList.add(`delay-${index % 3 + 1}`);
    });
  });
  
  // Function for date formatting
  function formatDate(date) {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(date).toLocaleDateString('en-US', options);
  }
  
  // Demo task creation function
  function addTask(event) {
    event.preventDefault();
    
    const taskInput = document.getElementById('new-task-input');
    const tasksList = document.querySelector('.tasks-body');
    
    if (taskInput.value.trim() === '') {
      return;
    }
    
    const taskHTML = `
      <div class="task-item">
        <div class="task-info">
          <h4>${taskInput.value}</h4>
          <p>Due: ${formatDate(new Date(Date.now() + 7 * 24 * 60 * 60 * 1000))}</p>
        </div>
        <span class="task-status status-pending">Pending</span>
        <div class="task-actions">
          <button><i class="fas fa-edit"></i></button>
          <button><i class="fas fa-trash"></i></button>
        </div>
      </div>
    `;
    
    tasksList.insertAdjacentHTML('beforeend', taskHTML);
    taskInput.value = '';
    
    // Add event listeners to new buttons
    const newTaskItem = tasksList.lastElementChild;
    const deleteBtn = newTaskItem.querySelector('.fa-trash').parentElement;
    deleteBtn.addEventListener('click', function() {
      newTaskItem.remove();
    });
  }
  
  // Attach task creation to form if it exists
  const taskForm = document.getElementById('new-task-form');
  if (taskForm) {
    taskForm.addEventListener('submit', addTask);
  }