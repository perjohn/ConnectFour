import { styled } from '@mui/material/styles';
import {Table, TableBody, TableContainer, TableRow} from "@mui/material";
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import Disc from "./Disc";


const rows = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 1, -1, 0, 0]
];

const StyledTableCell = styled(TableCell)(() => ({
    [`&.${tableCellClasses.body}`]: {
        height: '110px',
        width: '5em',
        border: '2px solid gray'
    }
}));

const Board = () => {
    return (
        <TableContainer style={{width: '770px'}}>
            <Table padding='none' aria-label="Het bord">
                <TableBody>
                    {rows.map((cells, rowIndex) => (
                        <TableRow
                            key={rowIndex}
                            sx={{  }}
                        >
                            {cells.map((cell, colIndex) => (
                                <StyledTableCell align='center'>
                                    {cell == 0 ? '' : <Disc player={cell === -1 ? 'yellow' : 'red'}/>}
                                </StyledTableCell>
                            ))}

                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    )
}

export default Board