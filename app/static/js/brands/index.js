$(document).ready(function() {

    $('#createBtn').on('click', function() {
        window.location.href = '/brands/create';
    });

    var url = window.location.href;
    url = url.split('/');
    console.log(url[5]);

    $.each($('.pag-btn'), function() {
        if ($(this).text() == url[5]) {
            $(this).removeClass('btn-primary-outline');
            $(this).addClass('btn-primary');
        }
    });

    $.ajax({
        type: 'GET',
        dataType: 'JSON',
        url: '/brands/fetch/' + url[5],
        success: function(data) {
            console.log(data);
            var tbody = $('<tbody></tbody>');
            $.each(data, function(index, value) {

                // Store each brands' properties
                var rowId = value.id;
                var title = value.title;
                var summary = value.summary;
                var createdById = value.created_by_id;
                var createdAt = value.created_at;
                var updatedAt = value.updated_at;

                // Create a row element
                var tr = $('<tr></tr>');

                // Delete button
                var deleteBtn = $('<button type="button" class="btn btn-danger form-control">Delete</button>');
                $(deleteBtn).on('click', function() {
                    window.location.href = '/brands/delete/' + rowId;
                });

                // Create row data elements
                var idTd = $('<td>' + rowId + '</td>');
                var titleTd = $('<td>' + title + '</td>');
                var summaryTd = $('<td>' + summary + '</td>');
                var createdByIdTd = $('<td>' + createdById + '</td>');
                var createdAtTd = $('<td>' + createdAt + '</td>');
                var updatedAtTd = $('<td>' + updatedAt + '</td>');
                var optionsTd = $('<td></td>');

                // Append buttons to options
                $(optionsTd).append($(deleteBtn));

                // Append row data to row
                tr.append(idTd);
                tr.append(titleTd);
                tr.append(summaryTd);
                tr.append(createdByIdTd);
                tr.append(createdAtTd);
                tr.append(updatedAtTd);
                tr.append(optionsTd);

                $('#brandsTable > tbody').append(tr);
                
                // Append to array
                // tbody.append(tr);
            });
            // $('#brandsTable > tbody').html(tbody);
        },
        error: function(error) {
            console.log(error);
        }
    });

    $('.pag-btn').on('click', function() {
        var page = $(this).text();
        window.location.href = '/brands/index/' + page;
    });
});