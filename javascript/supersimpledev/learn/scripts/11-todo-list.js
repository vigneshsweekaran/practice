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
  for (let i=0; i < todoList.length; i++) {
    todoObject = todoList[i]
    const html = `
      <div>${todoObject.name}</div>
      <div>${todoObject.dueDate}</div>
      <button onclick="removeTodoList(${i})" class="delete-todo-button">Delete</button>`;
    todoListHtml += html;
  }

  document.querySelector('.js-show-todolist').innerHTML = todoListHtml;
}

function removeTodoList(index) {
  todoList.splice(index, 1);
  renderTodoList();
}