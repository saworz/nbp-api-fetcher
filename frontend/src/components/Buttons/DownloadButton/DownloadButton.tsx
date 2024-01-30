import "./DownloadButton.css"
import { toast } from "react-toastify";


interface DownloadButtonProps {
  selectedCurrencies: string[];
  disabled: boolean
}


export const DownloadButton: React.FC<DownloadButtonProps> = ({ selectedCurrencies, disabled }) => {

  return (
    <div>
      <button>Download as csv</button>
    </div>
  );
};

export default DownloadButton;