import { Chip, Sheet, Button, Modal, ModalClose, Typography, ModalDialog, CircularProgress } from "@mui/joy";
import Table from "@mui/joy/Table";

import Shelf from "../types/shelf";
import { Link } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { useState } from "react";
import BookBadge from "../components/BookChip";
import ConnectionErrorModal from "../components/ConnectionErrorModal";

function ShelfList() {

  var { data, isLoading, isError } = useQuery({
    queryKey: ['shelves'],
    queryFn: () => fetch('http://localhost:8000/api/shelves').then(
      res => res.json()
    ),
  });

  data = data as Shelf[];

  if (isLoading) return  <CircularProgress value={10} />
  if (isError) return <ConnectionErrorModal />

  return (
    <div>
      <h1>Shelf List</h1>
      <Sheet>
        <Table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {data.map((shelf: Shelf) => (
              <tr key={shelf.id}>
                <td>{shelf.id}</td>
                <td>{shelf.name}</td>
                <td>{shelf.description}</td>
              </tr>
              ))
            }
          </tbody>
        </Table>
      </Sheet>
    </div>
  );
}

export default ShelfList;

