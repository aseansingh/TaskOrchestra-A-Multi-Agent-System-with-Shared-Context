import React, { useState } from 'react';

function TaskInput({ onResult }) {
  const [task, setTask] = useState('');

  const handleRun = async () => {
    if (!task.trim()) return;

    // Clear previous result before sending request
    onResult(null);

    try {
      const response = await fetch('http://localhost:8000/run', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_task: task }),
      });

      const data = await response.json();
      onResult(data);
    } catch (error) {
      console.error('Error:', error);
      onResult({ error: 'Failed to fetch result.' });
    }
  };

  return (
    <div>
      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        placeholder="What is your task?"
        style={{ padding: '0.5rem', width: '300px', marginRight: '1rem' }}
      />
      <button onClick={handleRun}>Run Task</button>
    </div>
  );
}

export default TaskInput;