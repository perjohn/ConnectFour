import React from 'react';
import './App.css';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import MainPage from "./components/MainPage";


const darkTheme = createTheme({
    palette: {
        mode: 'dark',
        primary: {
          main: '#232323'
        },
        secondary: {
            main: '#278a25'
        },
  },
});

function App() {
  return (
      <ThemeProvider theme={darkTheme}>
        <MainPage/>
      </ThemeProvider>
  );
}

export default App;
