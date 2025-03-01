import axios from 'axios';

export const sendAxiosRequest = async (url:string, data:object) => {
    try {
      const response = await axios.post(url, data,  {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      return response.data;
    } catch (error) {
      console.error('Error:', error);
      throw error;
    }
  };

 
export const downloadFile = async(url:string, filename:string) =>{
    try {
      const response = await axios.get(url, {
        responseType: 'blob', 
      });
      
      console.log(response)
      const urlBlob = window.URL.createObjectURL(new Blob([response.data]))
      const a = document.createElement('a');
      a.href = urlBlob;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(urlBlob);
    } catch (error) {
      console.error("Download error: ", error)
      throw error;
      
    }
}  
export const previewFile = async (url: string): Promise<string> => {
  try {
    const response = await axios.get(url, { responseType: 'blob' });
    
    const fileText = await response.data.text();
    return fileText;
  } catch (error) {
    console.error("Preview error: ", error);
    throw error;
  }
};

export default sendAxiosRequest;


//