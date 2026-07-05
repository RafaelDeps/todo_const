// UUID Generator
function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = Math.random() * 16 | 0;
        const v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

// Global State
let tasks = [];
let activeTab = 'tasks';
let activeFilter = 'all';
let searchQuery = '';
const notifiedTasks = new Set(); // Track tasks notified during this session

// DOM Elements
const elements = {
    navButtons: document.querySelectorAll('.nav-btn'),
    tabContents: document.querySelectorAll('.tab-content'),
    addTaskForm: document.getElementById('add-task-form'),
    tasksUl: document.getElementById('tasks-ul'),
    noTasksMsg: document.getElementById('no-tasks-msg'),
    statsPending: document.getElementById('stats-pending'),
    searchInput: document.getElementById('search-input'),
    filterButtons: document.querySelectorAll('.filter-btn'),
    toastContainer: document.getElementById('toast-container'),
    
    // Import/Export
    btnExport: document.getElementById('btn-export'),
    importForm: document.getElementById('import-task-form'),
    importFile: document.getElementById('import-file'),
    
    // Modal Edit
    editModal: document.getElementById('edit-modal'),
    editForm: document.getElementById('edit-task-form'),
    editId: document.getElementById('edit-id'),
    editTitle: document.getElementById('edit-title'),
    editDescription: document.getElementById('edit-description'),
    editReminder: document.getElementById('edit-reminder_at'),
    closeModalBtn: document.getElementById('close-modal-btn'),
    btnCancelEdit: document.getElementById('btn-cancel-edit')
};

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    loadTasks();
    setupEventListeners();
    requestNotificationPermission();
    render();
    
    // Start reminder checking interval (every 5 seconds)
    setInterval(checkReminders, 5000);
});

// Load tasks from localStorage
function loadTasks() {
    try {
        const data = localStorage.getItem('tasks');
        tasks = data ? JSON.parse(data) : [];
        if (!Array.isArray(tasks)) {
            tasks = [];
        }
    } catch (e) {
        showToast('Erro ao carregar tarefas do armazenamento local.', 'error');
        tasks = [];
    }
}

// Save tasks to localStorage
function saveTasks() {
    try {
        localStorage.setItem('tasks', JSON.stringify(tasks));
        return true;
    } catch (e) {
        showToast('Erro ao salvar tarefas localmente.', 'error');
        return false;
    }
}

// Show custom toast notification
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    const textNode = document.createElement('span');
    textNode.textContent = message;
    toast.appendChild(textNode);
    
    const closeNode = document.createElement('span');
    closeNode.className = 'toast-close';
    closeNode.innerHTML = '&times;';
    closeNode.onclick = () => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    };
    toast.appendChild(closeNode);
    
    elements.toastContainer.appendChild(toast);
    
    // Auto-remove after 4 seconds
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(20px) scale(0.9)';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

// Request permission for system notifications
function requestNotificationPermission() {
    if ('Notification' in window && Notification.permission === 'default') {
        Notification.requestPermission();
    }
}

// Event Listeners Setup
function setupEventListeners() {
    // Navigation Tabs
    elements.navButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.getAttribute('data-tab');
            switchTab(targetTab);
        });
    });
    
    // Form Submission: Add Task
    elements.addTaskForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const reminderAt = document.getElementById('reminder_at').value;
        
        // Validation
        if (!title || !title.trim()) {
            showToast('O título é obrigatório.', 'error');
            return;
        }
        if (title.length > 100) {
            showToast('O título deve ter no máximo 100 caracteres.', 'error');
            return;
        }
        if (reminderAt && new Date(reminderAt) <= new Date()) {
            showToast('O lembrete deve ser uma data futura.', 'error');
            return;
        }
        
        const newTask = {
            id: generateUUID(),
            title: title.trim(),
            description: description.trim(),
            reminder_at: reminderAt || null,
            status: 'pending',
            created_at: new Date().toISOString()
        };
        
        tasks.push(newTask);
        if (saveTasks()) {
            elements.addTaskForm.reset();
            render();
            showToast('Tarefa adicionada com sucesso.', 'success');
        }
    });
    
    // Form Submission: Edit Task
    elements.editForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const id = elements.editId.value;
        const title = elements.editTitle.value;
        const description = elements.editDescription.value;
        const reminderAt = elements.editReminder.value;
        
        // Validation
        if (!title || !title.trim()) {
            showToast('O título é obrigatório.', 'error');
            return;
        }
        if (title.length > 100) {
            showToast('O título deve ter no máximo 100 caracteres.', 'error');
            return;
        }
        if (reminderAt && new Date(reminderAt) <= new Date()) {
            showToast('O lembrete deve ser uma data futura.', 'error');
            return;
        }
        
        const taskIndex = tasks.findIndex(t => t.id === id);
        if (taskIndex !== -1) {
            tasks[taskIndex].title = title.trim();
            tasks[taskIndex].description = description.trim();
            // Reset notifications state if reminder date changed
            if (tasks[taskIndex].reminder_at !== (reminderAt || null)) {
                notifiedTasks.delete(id);
            }
            tasks[taskIndex].reminder_at = reminderAt || null;
            
            if (saveTasks()) {
                closeModal();
                render();
                showToast('Tarefa atualizada com sucesso.', 'success');
            }
        } else {
            showToast('Tarefa não encontrada.', 'error');
        }
    });
    
    // Search input
    elements.searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value.toLowerCase();
        render();
    });
    
    // Filter Buttons
    elements.filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            elements.filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            activeFilter = btn.getAttribute('data-filter');
            render();
        });
    });
    
    // Close Modal Events
    elements.closeModalBtn.addEventListener('click', closeModal);
    elements.btnCancelEdit.addEventListener('click', closeModal);
    window.addEventListener('click', (e) => {
        if (e.target === elements.editModal) {
            closeModal();
        }
    });
    
    // Export Data
    elements.btnExport.addEventListener('click', exportTasks);
    
    // Import Data
    elements.importForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const file = elements.importFile.files[0];
        if (!file) {
            showToast('Selecione um arquivo JSON.', 'error');
            return;
        }
        
        const mode = document.querySelector('input[name="import-mode"]:checked').value;
        const reader = new FileReader();
        
        reader.onload = function(event) {
            try {
                const importedData = JSON.parse(event.target.result);
                if (!Array.isArray(importedData)) {
                    showToast('Arquivo JSON inválido: o conteúdo deve ser uma lista de tarefas.', 'error');
                    return;
                }
                
                importTasks(importedData, mode);
            } catch (err) {
                showToast('Arquivo JSON inválido. Certifique-se de usar um arquivo tasks.json válido.', 'error');
            }
        };
        
        reader.readAsText(file);
    });
}

// Tab Switching
function switchTab(tabName) {
    activeTab = tabName;
    elements.navButtons.forEach(btn => {
        if (btn.getAttribute('data-tab') === tabName) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
    
    elements.tabContents.forEach(tab => {
        const id = tab.getAttribute('id');
        if (id === `tab-${tabName}`) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });
}

// Edit Modal actions
function openModal(task) {
    elements.editId.value = task.id;
    elements.editTitle.value = task.title;
    elements.editDescription.value = task.description || '';
    elements.editReminder.value = task.reminder_at || '';
    
    elements.editModal.classList.add('active');
}

function closeModal() {
    elements.editModal.classList.remove('active');
    elements.editForm.reset();
}

// Toggle Task Status
function toggleTask(id) {
    const taskIndex = tasks.findIndex(t => t.id === id);
    if (taskIndex !== -1) {
        const newStatus = tasks[taskIndex].status === 'pending' ? 'done' : 'pending';
        tasks[taskIndex].status = newStatus;
        if (saveTasks()) {
            render();
            showToast(`Tarefa marcada como ${newStatus === 'done' ? 'concluída' : 'pendente'}.`, 'success');
        }
    }
}

// Delete Task
function deleteTask(id) {
    if (confirm('Tem certeza de que deseja excluir esta tarefa?')) {
        tasks = tasks.filter(t => t.id !== id);
        notifiedTasks.delete(id);
        if (saveTasks()) {
            render();
            showToast('Tarefa excluída.', 'success');
        }
    }
}

// Export Tasks as JSON
function exportTasks() {
    const jsonStr = JSON.stringify(tasks, null, 2);
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = 'tasks.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    showToast('Download do backup tasks.json iniciado.', 'success');
}

// Import Tasks Data Logic
function importTasks(importedTasks, mode) {
    if (mode === 'replace') {
        tasks = importedTasks.map(t => ({
            id: t.id || generateUUID(),
            title: t.title || 'Tarefa sem Título',
            description: t.description || '',
            reminder_at: t.reminder_at || null,
            status: t.status === 'done' ? 'done' : 'pending',
            created_at: t.created_at || new Date().toISOString()
        }));
        if (saveTasks()) {
            elements.importForm.reset();
            switchTab('tasks');
            render();
            showToast('Todas as tarefas foram substituídas com sucesso.', 'success');
        }
    } else {
        // Smart Merge: Check uniqueness by signature (title, reminder_at)
        const existingSignatures = new Set(
            tasks.map(t => `${t.title.trim()}|||${t.reminder_at || ''}`)
        );
        
        let addedCount = 0;
        importedTasks.forEach(t => {
            const title = (t.title || '').trim();
            const reminder = t.reminder_at || '';
            const signature = `${title}|||${reminder}`;
            
            if (!existingSignatures.has(signature)) {
                tasks.push({
                    id: t.id || generateUUID(),
                    title: title,
                    description: t.description || '',
                    reminder_at: t.reminder_at || null,
                    status: t.status === 'done' ? 'done' : 'pending',
                    created_at: t.created_at || new Date().toISOString()
                });
                existingSignatures.add(signature);
                addedCount++;
            }
        });
        
        if (saveTasks()) {
            elements.importForm.reset();
            switchTab('tasks');
            render();
            showToast(`Mesclagem concluída. ${addedCount} novas tarefas importadas.`, 'success');
        }
    }
}

// Check reminders periodically
function checkReminders() {
    const now = new Date();
    
    tasks.forEach(task => {
        if (task.status !== 'done' && task.reminder_at) {
            const reminderTime = new Date(task.reminder_at);
            
            if (reminderTime <= now && !notifiedTasks.has(task.id)) {
                notifiedTasks.add(task.id);
                triggerReminderNotification(task);
            }
        }
    });
}

// Trigger Notifications
function triggerReminderNotification(task) {
    const message = `Lembrete: ${task.title}`;
    
    // System Notification if permitted
    if ('Notification' in window && Notification.permission === 'granted') {
        new Notification('Const Todo', {
            body: task.title,
            icon: 'assets/images/favicon.png' // Fallback to common icon if exists
        });
    } else {
        // Fallback to alert and inline notification styling
        alert(message);
    }
    
    // Visual Highlight & Toast
    showToast(message, 'info');
    render(); // Re-render to highlight overdue elements
}

// Helper to format ISO datetimes beautifully
function formatDateTime(isoString) {
    if (!isoString) return '';
    try {
        const dt = new Date(isoString);
        if (isNaN(dt.getTime())) return isoString;
        
        return dt.toLocaleString('pt-BR', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    } catch (e) {
        return isoString;
    }
}

// Render Tasks List UI
function render() {
    elements.tasksUl.innerHTML = '';
    
    // Stats calculation
    const pendingCount = tasks.filter(t => t.status === 'pending').length;
    elements.statsPending.textContent = `${pendingCount} pendente${pendingCount !== 1 ? 's' : ''}`;
    
    // Filter and Search
    const filteredTasks = tasks.filter(task => {
        // Filter by Status
        if (activeFilter === 'pending' && task.status !== 'pending') return false;
        if (activeFilter === 'completed' && task.status !== 'done') return false;
        
        // Search query check
        if (searchQuery) {
            const titleMatch = task.title.toLowerCase().includes(searchQuery);
            const descMatch = (task.description || '').toLowerCase().includes(searchQuery);
            return titleMatch || descMatch;
        }
        
        return true;
    });
    
    if (filteredTasks.length === 0) {
        elements.noTasksMsg.style.display = 'block';
        return;
    } else {
        elements.noTasksMsg.style.display = 'none';
    }
    
    // Sort tasks: pending first, then completed. Inside each, sorted by creation date descending
    filteredTasks.sort((a, b) => {
        if (a.status !== b.status) {
            return a.status === 'pending' ? -1 : 1;
        }
        return new Date(b.created_at) - new Date(a.created_at);
    });
    
    const now = new Date();
    
    filteredTasks.forEach(task => {
        const li = document.createElement('li');
        li.className = `task-item ${task.status === 'done' ? 'done' : ''}`;
        
        // Check if reminder is overdue
        let isOverdue = false;
        if (task.status !== 'done' && task.reminder_at) {
            const remTime = new Date(task.reminder_at);
            if (remTime <= now) {
                isOverdue = true;
                li.style.border = '1px solid rgba(244, 63, 94, 0.4)';
                li.style.boxShadow = '0 0 10px rgba(244, 63, 94, 0.15)';
            }
        }
        
        // Task checkbox
        const checkboxWrapper = document.createElement('div');
        checkboxWrapper.className = 'task-checkbox-wrapper';
        checkboxWrapper.onclick = () => toggleTask(task.id);
        
        const checkbox = document.createElement('div');
        checkbox.className = 'task-checkbox';
        checkboxWrapper.appendChild(checkbox);
        li.appendChild(checkboxWrapper);
        
        // Task details
        const details = document.createElement('div');
        details.className = 'task-details';
        
        const h3 = document.createElement('h3');
        h3.textContent = task.title;
        details.appendChild(h3);
        
        if (task.description) {
            const p = document.createElement('p');
            p.textContent = task.description;
            details.appendChild(p);
        }
        
        if (task.reminder_at) {
            const meta = document.createElement('div');
            meta.className = 'task-meta';
            
            const remBadge = document.createElement('span');
            remBadge.className = `reminder-badge ${isOverdue ? 'overdue' : ''}`;
            remBadge.innerHTML = `⏰ ${formatDateTime(task.reminder_at)}${isOverdue ? ' (Atrasado!)' : ''}`;
            
            meta.appendChild(remBadge);
            details.appendChild(meta);
        }
        
        li.appendChild(details);
        
        // Task actions
        const actions = document.createElement('div');
        actions.className = 'task-actions';
        
        // Edit button
        const btnEdit = document.createElement('button');
        btnEdit.className = 'action-btn btn-edit-task';
        btnEdit.innerHTML = '✏️';
        btnEdit.title = 'Editar';
        btnEdit.onclick = () => openModal(task);
        actions.appendChild(btnEdit);
        
        // Delete button
        const btnDelete = document.createElement('button');
        btnDelete.className = 'action-btn btn-delete-task';
        btnDelete.innerHTML = '🗑️';
        btnDelete.title = 'Excluir';
        btnDelete.onclick = () => deleteTask(task.id);
        actions.appendChild(btnDelete);
        
        li.appendChild(actions);
        
        elements.tasksUl.appendChild(li);
    });
}
