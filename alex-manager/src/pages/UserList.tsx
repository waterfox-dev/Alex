import {  Sheet,  CircularProgress } from "@mui/joy";
import Table from "@mui/joy/Table";

import User from "../types/user";
import { useQuery } from "@tanstack/react-query";
import ConnectionErrorModal from "../components/ConnectionErrorModal";

function ShelfList() {

  var { data, isLoading, isError } = useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('http://localhost:8000/api/users').then(
      res => res.json()
    ),
  });

  data = data as User[];

  if (isLoading) return  <CircularProgress value={10} />
  if (isError) return <ConnectionErrorModal />

  return (
    <div>
      <h1>User List</h1>
      <Sheet>
        <Table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Username</th>
              <th>Email</th>
              <th>First Name</th>
              <th>Last Name</th>
            </tr>
          </thead>
          <tbody>
            {data.map((shelf: User) => (
              <tr key={shelf.id}>
                <td>{shelf.id}</td>
                <td>{shelf.username}</td>
                <td>{shelf.email}</td>
                <td>{shelf.first_name}</td>
                <td>{shelf.last_name}</td>
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

