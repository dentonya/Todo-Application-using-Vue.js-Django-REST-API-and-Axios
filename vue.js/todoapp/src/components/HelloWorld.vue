<template>
  <div class="hello">
    <h1 class="title">TODO APP</h1> <!-- Page title -->

    <hr>

    <div class="columns">
      <div class="column is-one-third is-offset-one-third"> <!-- Narrow centered column -->
        <form><!-- Form for adding tasks -->
          <h2 class="subtitle">Add the task</h2>

          <div class="field"> <!-- Normal input field for the description -->
            <label class="label">Add Description</label>
            <div class="control">
              <input class="input" type="text">
            </div>
          </div>

          <div class="field"> <!-- Select field for choosing the status-->v
            <label class="label">Select Status</label>
            <div class="control">
              <div class="select">
                <select>
                  <option value="worktodo">Work To do</option>
                  <option value="workdone">Work Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field is-grouped"> <!-- Submit button -->
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <hr>

    <div class="columns">
      <div class="column is-half"> <!-- Half of the column for todo tasks -->
        <h2 class="subtitle">Task Todo</h2>

       <div class="todo">
      <div class="card" v-for="task in tasks" v-if="task.status == 'todo'"> <!-- Loop through the tasks array, if status is 'todo' then we'll show it. -->
        <div class="card-content">
          <div class="content">
            {{ task.work_description }} <!-- Print the task's description here -->
          </div>
        </div>

        <footer class="card-footer">
          <a class="card-footer-item">Work Done</a>
        </footer>
      </div>
    </div>
  </div>
  </div>

  <div class="column is-half">
    <h2 class="subtitle">Work Done</h2>

    <div class="done">
      <div class="card" v-for="task in tasks" v-if="task.status == 'done'"> <!-- Loop through the tasks array, if status is 'done'then we'll show it. -->
        <div class="card-content">
          <div class="content">
            {{ task.work_description }}
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data () {
    return {
      tasks: [] // Array for holding the tasks
    }
  },
  mounted () { // This will be called when HelloWorld is loaded
    this.get_Tasks(); // Call our getTasks function below
  },
  methods: {
    get_Tasks() {
        axios({
            method:'get',
            url: 'http://127.0.0.1:8000/tasks/',
            auth: {
                username: 'denatonya',
                password: 'ADMIN@123'
            }
        }).then(response => this.tasks = response.data);
    }
  }
}
</script>

<style scoped>
.select, select { /* 100% width for the select */
  width: 100%;
}

.card { /* Adding some air under the tasks */
  margin-bottom: 25px;
}

.done { /* Make the done tasks a little bit transparent */
  opacity: 0.3;
}
</style>