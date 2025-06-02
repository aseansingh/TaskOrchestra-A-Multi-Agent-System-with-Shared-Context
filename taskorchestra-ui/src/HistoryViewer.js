import React, { useEffect, useState } from 'react';

function HistoryViewer() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/history')
      .then(res => res.json())
      .then(setHistory)
      .catch(console.error);
  }, []);

  return (
    <div style={{ marginTop: '2rem' }}>
      <h2>Task History</h2>
      {history.length === 0 ? (
        <p>No tasks yet.</p>
      ) : (
        history.map((entry, idx) => (
          <div key={idx} style={{ marginBottom: '1rem' }}>
            <strong>Task:</strong> {entry.user_task} <br />
            <strong>Plan:</strong>
            <ul>
              {entry.plan.map((step, i) => (
                <li key={i}>{step}</li>
              ))}
            </ul>
            <strong>Summary:</strong>
            <pre style={{ backgroundColor: '#f8f8f8', padding: '0.5rem' }}>
              {entry.summary}
            </pre>
          </div>
        ))
      )}
    </div>
  );
}

export default HistoryViewer;