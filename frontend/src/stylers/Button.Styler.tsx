import styled from "styled-components";

export const Title = styled.h1`
margin-top:250px;
font-size: 15px;
`;

export const ButtonContainer = styled.button`
display: flex;
gap: 0px;
width: 40vw;
height: auto;
font-weight: bold;
background-width: 50vw;
font: bold;
background-color: white;
`;

export const ButtonSubtitle = styled.line`
font-size: 15px;
color: darkgray;
font-weight: normal;
line-height: 1.0;

`
export const StyledSubtitle = styled.line<{isActive: boolean}>`
color: ${({ isActive }) => (isActive ? "darkviolet" : "gray")}
`;

export const StyledButton = styled.div<{isActive: boolean}>`
padding: 10px 20px;
font-size: 20px;
font-weight: bold;
cursor: 'pointer';
width: 50vw;
color: black;
line-height: 0.15;

background-color: ${({ isActive }) => (isActive ? "beige" : "white")};
`;


