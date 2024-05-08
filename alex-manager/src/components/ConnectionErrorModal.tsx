import { Modal, ModalClose, ModalDialog, Typography } from "@mui/joy";
import { useState } from "react";


function ConnectionErrorModal() {
    const [open, setOpen] = useState<boolean>(true);
    return <Modal
        aria-labelledby="modal-title"
        aria-describedby="modal-desc"
        open={open}
        onClose={() => setOpen(false)}
        sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}
    >
        <ModalDialog
            variant="outlined"
            sx={{
                maxWidth: 500,
                borderRadius: 'md',
                p: 3,
                boxShadow: 'lg',
            }}
            color="danger"
        >
            <ModalClose variant="plain" sx={{ m: 1 }} />
            <Typography
                component="h2"
                id="modal-title"
                level="h4"
                textColor="inherit"
                fontWeight="lg"
                mb={1}
            >
                An error occured while fetching data
            </Typography>
            <Typography id="modal-desc" textColor="text.tertiary">
                Make sure your internet connection is stable and try again. If the problem persists, please contact the system administrator.
            </Typography>
        </ModalDialog>
    </Modal>
}

export default ConnectionErrorModal;