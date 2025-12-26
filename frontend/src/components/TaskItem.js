import React from 'react';
import { ListItem, ListItemText, IconButton, Paper } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';

function TaskItem({ task, onDelete }) {
  return (
    <Paper elevation={2} sx={{ mb: 2, p: 2 }}>
      <ListItem
        secondaryAction={
          <IconButton
            edge="end"
            onClick={() => onDelete(task.id)}
            aria-label="delete"
          >
            <DeleteIcon />
          </IconButton>
        }
      >
        <ListItemText
          primary={task.title}
          secondary={task.description}
        />
      </ListItem>
    </Paper>
  );
}

export default TaskItem;
