import React from 'react';
import { List, Typography } from '@mui/material';
import TaskItem from './TaskItem';

function TaskList({ tasks, onDeleteTask }) {
  if (tasks.length === 0) {
    return (
      <Typography variant="body1" sx={{ mt: 3, textAlign: 'center', color: 'text.secondary' }}>
        No tasks yet. Add one above!
      </Typography>
    );
  }

  return (
    <List sx={{ mt: 3 }}>
      {tasks.map((task) => (
        <TaskItem key={task.id} task={task} onDelete={onDeleteTask} />
      ))}
    </List>
  );
}

export default TaskList;
