<main>
  <div class="container">
    <h1 class="app-title">toDos</h1>
    <ul class="todo-list"></ul>
    <div class="empty-state">
      <svg class="checklist-icon"><use href="#checklist-icon"></use></svg>
      <h2 class="empty-state__title">Add your first todo</h2>
      <p class="empty-state__description">What do you want to get done today?</p>
    </div>
    <form on:submit|preventDefault={addTodo}>
      <input class="js-todo-input" type="text" aria-label="Enter a new todo item" placeholder="Grab Coffee with y" bind:value={newTodo}>
    </form>
    <ul class="todo-list">
      {#each todoItems as todo (todo.id)}
        <li class="todo-item {todo.checked ? 'done' : ''}">
          <input id={todo.id} type="checkbox" />
          <label for={todo.id} class="tick" on:click={() => toggleDone(todo.id)}></label>
          <span>{todo.text}</span>
        <button class="delete-todo" on:click={() => deleteTodo(todo.id)}>
          <svg><use href="#delete-icon"></use></svg>
        </button>
        </li>
      {/each}
    </ul>
  </div>
</main>

<script>
  import { afterUpdate } from 'svelte';

  afterUpdate(() => {
    document.querySelector('.js-todo-input').focus();
  });
  let todoItems = [];
  let newTodo = "";

  function addTodo(){
    newTodo = newTodo.trim();
    if (!newTodo) return;
  
    const todo = {
      text: newTodo,
      checked: false,
      id: Date.now()
    };
    todoItems = [...todoItems, todo];
    newTodo = "";
  }
//This is the completed function
  function toggleDone(id) {
  const index = todoItems.findIndex(item => item.id === Number(id));
  todoItems[index].checked = !todoItems[index].checked;
}
//This is the delete function
  function deleteTodo(id) {
    todoItems = todoItems.filter(item => item.id !== Number(id));
  }
</script>