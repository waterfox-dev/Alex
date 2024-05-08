import { Chip } from "@mui/joy";
import { Badge } from "@mui/joy";

import React from "react";


function BookChip({availability}: {availability: string}) {

    switch (availability) {
        case 'AVA':
            return <Chip color="success">Available</Chip>;
        case 'LOA':
            return <Chip color="danger">Loaned</Chip>;
        case 'RES':
            return <Chip color="warning">Reserved</Chip>;
        case 'LOS':
            return <Badge color="warning"><Chip color="danger">Lost</Chip></Badge>
        case 'STO' :
            return <Chip color="neutral">In Stock</Chip>;
        default:
            return <Chip color="primary"variant="solid">Unknown</Chip>;
    }

}

export default BookChip;