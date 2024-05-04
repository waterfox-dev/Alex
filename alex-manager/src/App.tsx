import React from 'react';

import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom';

import BookList from './pages/BookList';
import BookDetail from './pages/BookDetail';
import { Grid } from '@mui/joy';


function App() {
  return (
    <Grid container spacing={2} sx={{ flexGrow: 1 }}>
      <Grid xs={2}>
      <p>Menubar</p>
      </Grid>
      <Grid xs={9}>
      <Router>
        <Routes>
          <Route path="/books" element={<BookList/>}/>
          <Route path="/books/:id" element={<BookDetail/>}/>
        </Routes>
      </Router>
      </Grid>
    </Grid>
  );
}

export default App;
