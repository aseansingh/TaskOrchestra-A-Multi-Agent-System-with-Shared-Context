import React, { useState } from 'react';
import axios from 'axios';

function TaskInput({ onResult }) {
  const [task, setTask] = useState('');

  const handleRun = async () => {
    try {
      const response = await axios.post('http://localhost:8000/run', {
        user_task: task,
      });
      onResult(response.data);  // 👈 This calls App.js's handler
      setTask('');
    } catch (error) {
      console.error('Error running task:', error);
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="What is your task?"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        style={{ padding: '0.5rem', width: '300px' }}
      />
      <button onClick={handleRun} style={{ marginLeft: '1rem' }}>
        Run Task
      </button>
    </div>
  );
}

export default TaskInput;