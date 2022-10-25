import * as React from "react";
import {Button, Container, Grid} from "@mui/material";
import Board from "./Board";

const Content = () => {
    return (
        <Container sx={{minWidth: '100%', backgroundColor: 'primary.main', height: '100vh',justifyContent: 'center',}}>
            <Container sx={{
                display: 'flex',
                justifyContent: 'center',
                padding: '1em 0 1em 0',
                margin: 'auto'
            }}>
                <Board/>
            </Container>
            <Grid container>
                <Grid item xs={2}></Grid>
                <Grid item xs={4}>
                    <Button variant="contained" color='secondary'>Nieuw spel rood</Button>
                </Grid>
                <Grid item xs={4}>
                    <Button variant="contained" color='secondary'>Nieuw spel geel</Button>
                </Grid>
                <Grid item xs={2}></Grid>
            </Grid>
        </Container>
    )
}

export default Content;