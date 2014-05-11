(function($){

    $(function() {
        if ($(':hidden[name="admin_sorting_url"]').length > 0)
        {
            var tabular_inline_rows = $('.tabular table tbody tr');
            tabular_inline_rows.addClass('sortable');
            $('.tabular.inline-related').sortable({
                axis : 'y',
                containment : 'parent',
                create: function(event, ui) {
                    $('td.delete :checkbox').unbind();
                },
                tolerance : 'pointer',
                items : 'tr:not(.add-row)',
                stop : function(event, ui) {
                    if ($('.inline-deletelink').length > 0) {
                        $(ui.sender).sortable('cancel');
                        alert($('#localized_save_before_reorder_message').val());
                        return false;
                    }

                    var indexes = [];
                    ui.item.parent().children('tr').each(function(i)
                    {
                        var index_value = $(this).find('.original :hidden:first').val();
                        if (index_value !== '' && index_value !== undefined) {
                            indexes.push(index_value);
                        }
                    });

                    $.ajax({
                        url: ui.item.parent().find(':hidden[name="admin_sorting_url"]').val(),
                        type: 'POST',
                        data: { indexes : indexes.join(',') },
                        success: function() {
                            //highlight sorted row, then re-stripe table
                            ui.item.effect('highlight', {}, 1000);
                            tabular_inline_rows.removeClass('row1 row2');
                            $('.tabular table tbody tr:odd').addClass('row2');
                            $('.tabular table tbody tr:even').addClass('row1');
                        }
                    });
                }
            });
        }
    });

})(django.jQuery);
