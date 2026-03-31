document.addEventListener("DOMContentLoaded", () => {
  const inputField = document.getElementById("task-field");
  const addButton = document.getElementById("task-add");
  const tasksList = document.getElementById("tasks-container");
  const hideButton = document.getElementById("showall");
  const showButton = document.getElementById("hideall");

  const startingTasks = [
    { text: "Thomas 10.2 chap", done: true },
    { text: "Second Item", done: false },
    { text: "Third Item", done: false },
  ];

  showButton.addEventListener("click", () => {
  tasksList.style.display = "none";
});

hideButton.addEventListener("click", () => {
  tasksList.style.display = "";
});


  startingTasks.forEach((task) => createTask(task.text, task.done));

  addButton.addEventListener("click", () => {
    const text = inputField.value.trim();
    if (text) {
      createTask(text);
      inputField.value = "";
      inputField.focus();
    }
  });

  inputField.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      const text = inputField.value.trim();
      if (text) {
        createTask(text);
        inputField.value = "";
      }
    }
  });

  function createTask(text, done = false) {
    const li = document.createElement("li");
    li.className = "task-item";
    if (done) li.classList.add("completed");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.className = "task-check";
    checkbox.checked = done;
    checkbox.addEventListener("change", () => li.classList.toggle("completed"));

    const span = document.createElement("span");
    span.className = "task-text";
    span.textContent = text;

    const delBtn = document.createElement("img");
    delBtn.className = "task-del";
    delBtn.src = "delete.png";
    delBtn.alt = "Delete";   
    delBtn.addEventListener("click", () => tasksList.removeChild(li));

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(delBtn);
    tasksList.appendChild(li);
  }
});
