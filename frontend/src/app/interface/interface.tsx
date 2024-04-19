interface Item {
  key: string;
  id: number;
  part_no: string;
  plc_data: string;
  image_path: any;
  update_at: string;
}

interface EditableCellProps extends React.HTMLAttributes<HTMLElement> {
  editing: boolean;
  dataIndex: string;
  title: any;
  inputType: "number" | "text";
  record: Item;
  index: number;
  children: React.ReactNode;
}

type EditData = {
  line_id: any;
  process_id: any;
  part_no: string;
  plc_data: string;
  image_path: any;
};

type UpData = {
  id: number;
  
  part_no: string;
  plc_data: string;
  image_path: any;
  update_at: string;
};

type id_row = {
  id: number;
};

