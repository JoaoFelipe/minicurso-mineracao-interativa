from IPython.display import display, Javascript

JAVASCRIPT = """

var TITLE_PREFIX = "Mineração Interativa - " + IPython.notebook.get_notebook_name()

function scrollToCell(cell) {
    $('#site').animate({
        scrollTop: cell.element.position().top
    }, 500);
    
}
function scrollToSelected() {
    var cell = IPython.notebook.get_selected_cell()
    scrollToCell(cell);
    cell.focus_cell();
}

function selectCell(index) {
    var cells = IPython.notebook.get_cells();
    IPython.notebook.select(index);
    var cell = IPython.notebook.get_selected_cell();
    cell.element.toggle(true);

    var rx = /# skip-execution/g;
    var match = rx.exec(cell.get_text());
    if (cell.cell_type == "code" && match == undefined) {
        cell.execute();
    }
    
    
    if (cell.cell_type == "markdown") {
        var header = $(cell.get_rendered()).filter("h1, h2, h3, h4, h5, h6");
        if (header.length > 0) {
            var text = $(header[header.length - 1]).clone().children().remove().end().text();
            $("#current-title").text(TITLE_PREFIX + " - " + text);
        } else {
            header = $(cell.get_rendered()).find("h1, h2, h3, h4, h5, h6");
            if (header.length > 0) {
                var text = $(header[header.length - 1]).clone().children().remove().end().text();
                $("#current-title").text(TITLE_PREFIX + " - " + text);
            }
        }
    }
    
    
    var scrollIndex = undefined;
    rx = /<span class=\"notebook-slide-no-scroll\"\/>/g;
    match = rx.exec(cell.get_text());
    if (match == undefined && cell.cell_type == "markdown") {
        scrollIndex = index;
        rx = /<span class=\"notebook-slide-scroll\" data-position=\"(.*)?\"\/>/g;
        match = rx.exec(cell.get_text());
        if (match != undefined) {
            var n = parseInt(match[1]);
            scrollIndex += n;
        }
        scrollToCell(cells[scrollIndex]);
    }

    rx = /<span class=\"notebook-slide-extra\" data-count=\"(.*)?\"\/>/g;
    match = rx.exec(cell.get_text());
    if (match != undefined) {
        var n = parseInt(match[1]);
        for (var i = index + 1; i <= index + n; i++) {
            cell = cells[i];
            cell.element.toggle(true);
        }
    }

    $("#current-slide").text((index + 1) + "/" + (cells.length));
    
}


var hide = {
    icon: 'fa-eye-slash',
    help    : 'Hide all',
    help_index : 'zz',
    handler : function () {
        var cells = IPython.notebook.get_cells();
        var found = 0;
        var i = 0;
        for (var cell of IPython.notebook.get_cells()) {
            cell.element.toggle(false);
            var rx = /<span class=\"notebook-slide-start\"\/>/g;
            var match = rx.exec(cell.get_text());
            if (match) {
                found = i;
            }
            i += 1;
        }
        for (i = 0; i <= found; i++) {
            var cell = cells[i];
            cell.element.toggle(true);   
        }
        var cell = cells[cells.length - 1];
        cell.element.toggle(true);
        
        $(".navbar-nav").toggle(false);
        $("#slide-top").remove();
        $(".navbar-collapse").append("<div id='slide-top' style='padding: 6px 20px; text-align: center;'></div>")
        $("#slide-top").append("<div  style='float: left;' id='current-slide'>1</div>")
        $("#slide-top").append("<div style='display: inline-block; padding: 0 20px;' id='current-title'>"+ TITLE_PREFIX +"</div>")
        $("#slide-top").append("<div style='display: inline-block; padding: 0 20px; float: right;' id='current-name'>João Felipe Pimentel</div>")
        selectCell(found);
        document.documentElement.requestFullscreen();
    }
};
var show = {
    icon: 'fa-eye',
    help    : 'Show all',
    help_index : 'zz',
    handler : function () {
        for (var cell of IPython.notebook.get_cells()) {
          cell.element.toggle(true);
        }
        $("#slide-top").remove();
        $(".navbar-nav").toggle(true);
        
        document.exitFullscreen();
    }
};
var view = {
    icon: 'fa-eye',
    help    : 'Show cell',
    help_index : 'zz',
    handler : function () {
        selectCell(IPython.notebook.get_selected_index());
    }
};

var previous = {
    icon: 'fa-arrow-left',
    help    : 'Previous slide',
    help_index : 'zz',
    handler : function () {
        var cell = IPython.notebook.get_selected_cell();
        cell.element.toggle(false);
        var index = IPython.notebook.get_selected_index();
        selectCell(index - 1);
        IPython.notebook.select(index - 1);
        IPython.notebook.get_selected_cell().element.toggle(true);
        scrollToSelected();
    }
};
var next = {
    icon: 'fa-arrow-right',
    help    : 'Previous slide',
    help_index : 'zz',
    handler : function () {
        
        var index = IPython.notebook.get_selected_index();
        selectCell(index + 1);
        
    }
};
var prefix = 'slide-notebook';
var actions = Jupyter.actions

IPython.notebook.keyboard_manager.command_shortcuts.add_shortcut(
    '[', actions.register(previous, 'previous-slide', prefix)
)
IPython.notebook.keyboard_manager.command_shortcuts.add_shortcut(
    ']', actions.register(next, 'next-slide', prefix)
)
IPython.notebook.keyboard_manager.command_shortcuts.add_shortcut(
    '-', actions.register(hide, 'hide-all', prefix)
)
IPython.notebook.keyboard_manager.command_shortcuts.add_shortcut(
    '=', actions.register(show, 'show-all', prefix)
)
IPython.notebook.keyboard_manager.command_shortcuts.add_shortcut(
    '0', actions.register(view, 'show-cell', prefix)
)
"""

def load_ipython_extension(shell):
    display(Javascript(JAVASCRIPT))