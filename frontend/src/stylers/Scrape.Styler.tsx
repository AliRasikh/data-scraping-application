import styled from "styled-components";

export const ScrapeButtonContainer = styled.button`
position: absolute;
  top: 100%; /* Etwas unter den anderen Buttons */
  left: 50%;
  transform: translate(-50%, -50%);
  width: 200px;
  padding: 12px 20px;
  font-size: 16px;
  font-weight: bold;
  background-color: darkblue;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;

  &:hover {
    background-color: navy;
    transform: translate(-50%, -50%) scale(1.05);
    }

`;
