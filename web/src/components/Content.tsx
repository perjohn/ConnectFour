import * as React from "react";
import {Container} from "@mui/material";
import Board from "./Board";

const Content = () => {
    return (
        <Container sx={{
            display: 'flex',
            height: '100vh',
            minWidth: '100%',
            justifyContent: 'center',
            backgroundColor: 'primary.main',
            paddingTop: '1em'
        }}>
            <Board/>
        </Container>
    )
}

export default Content;