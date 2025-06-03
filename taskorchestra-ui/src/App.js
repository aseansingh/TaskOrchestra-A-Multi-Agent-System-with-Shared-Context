import React, { useState } from 'react';
import TaskInput from './TaskInput';
import HistoryViewer from './HistoryViewer';

function App() {
  const [result, setResult] = useState(null);

  const handleResult = (newResult) => {
    setResult(null); // 👈 Clear previous result before setting new one
    setTimeout(() => setResult(newResult), 0); // ensure UI updates
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>TaskOrchestra – Multi-Agent System</h1>
      <TaskInput onResult={handleResult} />
      {result && (
        <div style={{ marginTop: '2rem' }}>
          <h2>Final Shared Context</h2>
          <pre style={{ backgroundColor: '#f4f4f4', padding: '1rem' }}>
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
      <HistoryViewer />
    </div>
  );
}

export default App;