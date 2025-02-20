import  { ReactElement } from 'react'
import {HeaderContainer,SubTitleContainer} from '../stylers/Heading.Styler'

type HeadingProps = { 
    title: string
    subtitle: string}

const Heading = ({ title, subtitle }: HeadingProps): ReactElement => {
  return (
    <>
    <HeaderContainer>
        <h1>{title}</h1>
        {subtitle &&<SubTitleContainer>{subtitle}</SubTitleContainer>}
        </HeaderContainer>
    </>
  ) 
}
export default Heading