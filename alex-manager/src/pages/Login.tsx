import * as React from 'react';
import Sheet from '@mui/joy/Sheet';
import CssBaseline from '@mui/joy/CssBaseline';
import Typography from '@mui/joy/Typography';
import FormControl from '@mui/joy/FormControl';
import FormLabel from '@mui/joy/FormLabel';
import Input from '@mui/joy/Input';
import Button from '@mui/joy/Button';

import ApiToken from '../utils/ApitToken';

async function GetToken(username: string, password: string){
  ApiToken.setCreds(username, password);
  
  localStorage.setItem('token', ApiToken.getToken());
}


function Login() {

  var username: string = ''; 
  var password: string = '';

  return (
    <main>
      <CssBaseline />
      <Sheet
        sx={{
          width: 300,
          mx: 'auto', // margin left & right
          my: 4, // margin top & bottom
          py: 3, // padding top & bottom
          px: 2, // padding left & right
          display: 'flex',
          flexDirection: 'column',
          gap: 2,
          borderRadius: 'sm',
          boxShadow: 'md',
        }}
        variant="outlined"
      >
        <div>
          <Typography level="h4" component="h1">
            <b>Welcome!</b>
          </Typography>
          <Typography level="body-sm">Sign in to continue.</Typography>
        </div>
        <form onSubmit={(event)=>{
            event.preventDefault();
            const form = new FormData(event.currentTarget);
            username = form.get('username') as string;
            password = form.get('password') as string;
            GetToken(username, password);
          }}>
          <FormControl>
            <FormLabel>Username</FormLabel>
            <Input
              // html input attribute
              name="username"
              type="text"
              placeholder="johndoe@email.com"
              
            />
          </FormControl>
          <FormControl>
            <FormLabel>Password</FormLabel>
            <Input
              // html input attribute
              name="password"
              type="password"
              placeholder="password"
            />
          </FormControl>
          <Button type="submit" sx={{ mt: 1 /* margin top */ }}>Log in</Button>
        </form>
      </Sheet>
    </main>
  );
}

export default Login;