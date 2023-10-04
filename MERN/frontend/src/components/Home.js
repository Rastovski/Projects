import * as React from 'react';
import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import "../styles/Home.css"
import {useState, useEffect} from 'react'

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14, 
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  '&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
  },
  // hide last border
  '&:last-child td, &:last-child th': {
    border: 0,
  },
}));

const Home =()=>{

    const [rows, setRows] = useState([])

    useEffect(()=>{
        fetch("/api/workouts/")
        .then((response)=>response.json())
        .then((data)=>setRows(data))
        .catch((err)=> console.log(err))
    },[])

    let content = rows.map((row) => (
        <StyledTableRow key={row.title+row.date}>
          <StyledTableCell component="th" scope="row">
            {row.title}
          </StyledTableCell>
          <StyledTableCell align="right">{row.time}</StyledTableCell>
          <StyledTableCell align="right">{row.date.slice(0,row.date.indexOf("T"))}</StyledTableCell>
        </StyledTableRow>
      ))

  return (
    <>
    
    <div className='table'>
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHead>
          <TableRow>
            <StyledTableCell>Workout</StyledTableCell>
            <StyledTableCell align="right">Total time</StyledTableCell>
            <StyledTableCell align="right">Date</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
        {content}
        </TableBody>
      </Table>
    </TableContainer>
    
    </div>
  
  </>
  );
}

export default Home;