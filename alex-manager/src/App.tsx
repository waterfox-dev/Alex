import React from 'react';

import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom';

import BookList from './pages/BookList';
import BookDetail from './pages/BookDetail';
import ShelvesList from './pages/ShelvesList';
import MenuBar from './components/MenuBar';
import AuthorList from './pages/AuthorsList';
import Login from './pages/Login';

import { Grid } from '@mui/joy';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient()

function App() {
  return (
    <Router>
      <QueryClientProvider client={queryClient}>
      <Grid container  sx={{ flexGrow: 1 }}>
        <Grid xs={2}>
          <MenuBar />
        </Grid>
        <Grid xs={9}>
          <Routes>
            <Route path="/books" element={<BookList />} />
            <Route path="/books/:id" element={<BookDetail />} />
            <Route path="/shelves" element={<ShelvesList/>} />
            <Route path="/authors" element={<AuthorList/>} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </Grid>
      </Grid>
      </QueryClientProvider>
    </Router>

  );
}

export default App;
