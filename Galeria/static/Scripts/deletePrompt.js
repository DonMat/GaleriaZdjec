function deleteAlbum() {
showDeleteDialog("Twój album oraz zawarte w nim zdjęcia zostaną bezpowrotnie usunięte, czy kontynuować?")
}
function deletePicture() {
    showDeleteDialog("Twoje zdjęcie zostanie trwale usunięte, czy kontynuować?")
}

function showDeleteDialog(message){
        BootstrapDialog.show({
        type: BootstrapDialog.TYPE_DANGER,
        title: 'Potwierdź usuwanie',
        cssClass: '',
        message: message,
        buttons: [
            {
                label: 'Usuń',
                cssClass: 'btn-danger',
                action: function () {
                    $(location).attr('href', "./delete");
                }
            },
            {
                label: 'Cancel',
                action: function (dialog) {
                    dialog.close();
                }
            }
        ]
    });
}