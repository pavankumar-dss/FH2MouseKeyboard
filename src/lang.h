// The mod's text in the game's language, through the platform's translations (API 10, 2.9.0).
//
// The English is in the code; the translations are gettext PO files in l10n/, looked up by their
// English (no msgctxt; the mod's description has the key the platform looks it up by,
// "mod.description"). They're built into the DLL as src/fh2mouse_l10n.inc:
//
//   python3 platform/tools/l10n/po2inc.py src/fh2mouse_l10n.inc fh2mouse_translations l10n/*.po
//
// Text from tr() that goes to the platform as it is (a row's label, description and choices)
// follows the game's language by itself, so rows made at fh2mod_init are right once the game picks
// its language. Czech and Hungarian stay English, as the game's own text is there: their files
// are in l10n/held-back, not built in. On a platform before 2.9.0 everything is English.
// The key names ("Space", "LShift"...) stay as they are: they're the ini's.
#pragma once
#include "fh2mod_l10n.h"

#include <cstring>
#include <mutex>
#include <utility>
#include <vector>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable : 4125)   // po2inc's "\202" followed by a digit: an octal escape ends at 3 digits anyway
#endif
#include "fh2mouse_l10n.inc"
#ifdef _MSC_VER
#pragma warning(pop)
#endif

namespace lang {

inline const FH2ModApi* g_api = nullptr;
inline FH2Mod* g_mod          = nullptr;
inline std::mutex g_mu;
inline std::vector<std::pair<const char*, const char*>> g_given;   // what tr() gave, and its English (g_mu)

// Straight after register_mod: the translations go to the platform.
inline void init(const FH2ModApi* api, FH2Mod* mod) {
    g_api = api;
    g_mod = mod;
    FH2_ADD_TRANSLATIONS(api, mod, fh2mouse_translations);
}

// `english` in the game's language now; itself when there's no translation (or before init).
inline const char* tr(const char* english) {
    if (!english || !g_mod) return english;
    const char* t = fh2_tr(g_api, g_mod, nullptr, english);
    if (t != english) {
        std::scoped_lock lk{g_mu};
        bool known = false;
        for (const auto& [given, en] : g_given) known = known || given == t;
        if (!known) g_given.emplace_back(t, english);
    }
    return t;
}

// The English of a text tr() gave (or the text itself, if it isn't one of them).
inline const char* english(const char* text) {
    std::scoped_lock lk{g_mu};
    for (const auto& [given, en] : g_given)
        if (given == text) return en;
    return text;
}

} // namespace lang
