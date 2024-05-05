import { Chip, Sheet, Button, Modal, ModalClose, Typography, ModalDialog } from "@mui/joy";
import Table from "@mui/joy/Table";

import Book from "../types/book";
import { Link } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { useState } from "react";

function BookList() {

  const [open, setOpen] = useState<boolean>(true);

  var { data, isLoading, isError } = useQuery({
    queryKey: ['books'],
    queryFn: () => fetch('http://localhost:8000/api/books').then(
      res => res.json()
    ),
  });

  data = data as Book[];

  if (isLoading) return <div>Loading...</div>
  if (isError) return <Modal
      aria-labelledby="modal-title"
      aria-describedby="modal-desc"
      open={open}
      onClose={() => setOpen(false)}
      sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}
    >
    <ModalDialog
      variant="outlined"
      sx={{
        maxWidth: 500,
        borderRadius: 'md',
        p: 3,
        boxShadow: 'lg',
      }}
      color="danger"
    >
      <ModalClose variant="plain" sx={{ m: 1 }} />
      <Typography
        component="h2"
        id="modal-title"
        level="h4"
        textColor="inherit"
        fontWeight="lg"
        mb={1}
      >
        An error occured while fetching data
      </Typography>
      <Typography id="modal-desc" textColor="text.tertiary">
        Make sure your internet connection is stable and try again. If the problem persists, please contact the system administrator.
      </Typography>
    </ModalDialog>
  </Modal>

  return (
    <div>
      <h1>Book List</h1>
      <Sheet>
        <Table>
          <thead>
            <tr>
              <th>ID</th>
              <th>ISBN</th>
              <th>Title</th>
              <th>Shelf</th>
              <th>Author</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {data.map((book: Book) => (
              <tr key={book.id}>
                <td>{book.id}</td>
                <td>{book.isbn}</td>
                <td>{book.title}</td>
                <td>{book.shelf.name}</td>
                <td>{book.authors.map((author) => author.name + " " + author.first_name).join(', ')}</td>
                <td>
                  {book.availability.id === 1 ?
                    <Chip color="success">{book.availability.name}</Chip> : <Chip color="danger">{book.availability.name}</Chip>
                  }
                </td>
                <td>
                  <Link to={`/books/${book.id}`}><Button>Detail</Button></Link>
                </td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Sheet>
    </div>
  );
}

export default BookList;

