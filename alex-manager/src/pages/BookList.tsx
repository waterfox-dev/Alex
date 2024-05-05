import { Chip, Sheet, Button } from "@mui/joy";
import Table from "@mui/joy/Table";

import Book from "../types/book";
import { Link } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";

function BookList() {

  var { data, isLoading, isError } = useQuery({
    queryKey: ['books'],
    queryFn: () => fetch('http://localhost:8000/api/books').then(
      res => res.json()
    ),
  });

  data = data as Book[];
  
  if (isLoading) return <div>Loading...</div>
  if (isError) return <div>Error...</div>

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

