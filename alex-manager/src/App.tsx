import React from 'react';

import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom';

import BookList from './pages/BookList';
import BookDetail from './pages/BookDetail';
import MenuBar from './components/MenuBar';

import { Grid } from '@mui/joy';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient()

function App() {
  return (
    <Router>
      <QueryClientProvider client={queryClient}>
      <Grid container spacing={2} sx={{ flexGrow: 1 }}>
        <Grid xs={2}>
          <MenuBar />
        </Grid>
        <Grid xs={9}>
          <Routes>
            <Route path="/books" element={<BookList />} />
            <Route path="/books/:id" element={<BookDetail />} />
          </Routes>
        </Grid>
      </Grid>
      </QueryClientProvider>
    </Router>

  );
}

export default App;
