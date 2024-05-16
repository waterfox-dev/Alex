import { Sheet,  CircularProgress } from "@mui/joy";
import Table from "@mui/joy/Table";

import Author from "../types/author";
import { useQuery } from "@tanstack/react-query";
import ConnectionErrorModal from "../components/ConnectionErrorModal";



function AuthorsList() {

  var { data, isLoading, isError } = useQuery({
    queryKey: ['shelves'],
    queryFn: () => fetch('http://localhost:8000/api/authors').then(
      res => res.json()
    ),
  });

  data = data as Author[];

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
              <th>First Name</th>
            </tr>
          </thead>
          <tbody>
            {data.map((author: Author) => (
              <tr key={author.id}>
                <td>{author.id}</td>
                <td>{author.name}</td>
                <td>{author.first_name}</td>
              </tr>
              ))
            }
          </tbody>
        </Table>
      </Sheet>
    </div>
  );
}

export default AuthorsList;

