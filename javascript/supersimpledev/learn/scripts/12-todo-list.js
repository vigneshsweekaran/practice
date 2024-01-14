const todoList = [];

function addTodo() {
  const inputNameElement = document.querySelector('.js-name-input')
  const inputDateElement = document.querySelector('.js-due-date-input')
  const name = inputNameElement.value;
  const dueDate = inputDateElement.value;
  const todoObject = {name, dueDate}
  todoList.push(todoObject);
  inputNameElement.value = '';
  console.log(todoList);

  renderTodoList();

}

function renderTodoList() {
  let todoListHtml = '';

  todoList.forEach((todoObject) => {
    const html = `
      <div>${todoObject.name}</div>
      <div>${todoObject.dueDate}</div>
      <button class="delete-todo-button js-delete-todo-button">Delete</button>`;
    todoListHtml += html;
  });

  document.querySelector('.js-show-todolist').innerHTML = todoListHtml;
  document.querySelectorAll('.js-delete-todo-button')
    .forEach((deleteButton, index) => {
      deleteButton.addEventListener('click', () => {
        todoList.splice(index, 1);
        renderTodoList();
      });
    });
}

document.querySelector('.js-add-todo-button')
  .addEventListener('click', () => {
    addTodo();
  });