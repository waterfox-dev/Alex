import React from "react";
import {Divider, List, ListItem, ListItemButton, ListItemContent } from "@mui/joy";
import { Link } from "react-router-dom";

function MenuBar() {
  return (
    <List>
      <Link to="/" style={{ textDecoration: 'none', textDecorationColor: 'none' }}>
      <ListItem variant="soft">
          <ListItemButton>
            <ListItemContent>Home</ListItemContent>
          </ListItemButton>
      </ListItem>
      </Link>
      <Divider />
      <Link to="/books" style={{ textDecoration: 'none', textDecorationColor: 'none' }}>
        <ListItem variant="soft">
            <ListItemButton>
              <ListItemContent>Books</ListItemContent>
            </ListItemButton>
        </ListItem>
      </Link>
      <ListItem variant="soft">
        <ListItemButton>
          <ListItemContent>Shelves</ListItemContent>
        </ListItemButton>
      </ListItem>
      <ListItem variant="soft">
        <ListItemButton>
          <ListItemContent>Author</ListItemContent>
        </ListItemButton>
      </ListItem>
    </List>
  );
}

export default MenuBar;