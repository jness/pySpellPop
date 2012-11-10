import enchant
import gtk

class Spell:
    def __init__(self):
        self.dict = enchant.Dict('en_US')
        self.clip = gtk.Clipboard()

    def responseToDialog(self, entry, dialog, response):
        dialog.response(response)

    def getText(self, results=None):
        dialog = gtk.MessageDialog(
            None,
            gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
            gtk.MESSAGE_QUESTION,
            gtk.BUTTONS_OK,
            None)
        dialog.set_title('pySpellPop')
        dialog.set_markup('Welcome to pySpellPop')
        entry = gtk.Entry()
        entry.connect("activate", self.responseToDialog, dialog, gtk.RESPONSE_OK)
        hbox = gtk.HBox()
        if results:
            res = '\n'.join([ str(i) for i in enumerate(results) ])
            dialog.format_secondary_markup("Supply item # you wish to copy to clipboard:\n\n" + res)
        hbox.pack_start(gtk.Label("Input:"), False, 5, 5)
        hbox.pack_end(entry)
        dialog.vbox.pack_end(hbox, True, True, 0)
        dialog.show_all()
        dialog.run()
        text = entry.get_text()
        dialog.destroy()
        return text

def main():
    s = Spell()
    text = s.getText()
    res = s.dict.suggest(text)

    num = s.getText(res)
    s.clip.set_text(res[int(num)])
    s.clip.store()

if __name__ == '__main__':
    main()