import React from "react";
import { Divider, List, ListItem, ListItemButton, ListItemContent } from "@mui/joy";
import { Link } from "react-router-dom";

import { HiHome } from "react-icons/hi";
import { HiOutlineBookOpen } from "react-icons/hi";
import { HiOutlineCollection } from "react-icons/hi";
import { HiOutlineUsers } from "react-icons/hi";
import { HiOutlineUser } from "react-icons/hi";

function MenuBar() {
  return (
    <List>
      <Link to="/" style={{ textDecoration: 'none', textDecorationColor: 'none' }}>
        <ListItem variant="plain">
          <ListItemButton>
            <ListItemContent><HiHome /> Home</ListItemContent>
          </ListItemButton>
        </ListItem>
      </Link>
      <Divider />
      <Link to="/books" style={{ textDecoration: 'none', textDecorationColor: 'none' }}>
        <ListItem variant="plain">
          <ListItemButton>
            <ListItemContent><HiOutlineBookOpen /> Books</ListItemContent>
          </ListItemButton>
        </ListItem>
      </Link>
      <Link to="/shelves" style={{ textDecoration: 'none', textDecorationColor: 'none' }}>
        <ListItem variant="plain">
          <ListItemButton>
            <ListItemContent><HiOutlineCollection /> Shelves</ListItemContent>
          </ListItemButton>
        </ListItem>
      </Link>
      <Link to="/authors" style={{ textDecoration: 'none', textDecorationColor: 'none' }}>
        <ListItem variant="plain">
          <ListItemButton>
            <ListItemContent><HiOutlineUsers /> Authors</ListItemContent>
          </ListItemButton>
        </ListItem>
      </Link>
      <Divider />
      <Link to="users" style={{ textDecoration: 'none', textDecorationColor: 'none' }}>
        <ListItem variant="plain">
          <ListItemButton>
            <ListItemContent><HiOutlineUser /> User</ListItemContent>
          </ListItemButton>
        </ListItem>
      </Link>
    </List>
  );
}

export default MenuBar;