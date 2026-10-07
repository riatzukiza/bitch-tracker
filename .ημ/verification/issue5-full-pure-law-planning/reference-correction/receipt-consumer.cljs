(ns bitch5-reference-correction-receipt
 (:require [clojure.string :as str] [eta-mu.receipt-river.api :as api]
 [eta-mu.receipt-river.domain.receipt :as receipt] [eta-mu.receipt-river.shape.edn :as edn]
 ["node:fs" :as fs] ["node:child_process" :as child]))
(let [[mode target] *command-line-args*]
 (if (= mode "append")
  (let [now (.toISOString (js/Date.))
        payload (receipt/build-payload
          {:kind :adjudication :owner "root/issues" :origin "Codex isolated whole Bitch5 planning reference correction"
           :dod "Restore22missingnative references exact; explicitly bind6private setup records to original private hash/location/nonreviewscope; preserve entire7concepts8invariants7proof plus original7reactionAC and proposed13 decomposition"
           :pi "pr-sprint-planning+receipt-river" :host "new-independent-complete-persistent-correction-worktree"
           :manifest ".ημ/verification/issue5-full-pure-law-planning/native .ημ/verification/issue5-full-pure-law-planning/reference-correction .ημ/verification/issue5-full-pure-law-planning/README.md .ημ/receipts.edn .ημ/session-mycology/ledger.md"
           :refs "parent:9a9a84464297745b88bcb5a102395c96386d62f6 stack:64af437938b15b0e0bd37c80cc01610a1dc25992 issue:octave-commons/bitch-tracker5 RR:154440f3c997aa9208194bba59b5edbef3654f78 independentpeer:bitch5-full-laws-peer-t8yi59oi"
           :tests "All22recorded original encoded bytes/decoded hashes sizes exact,6existing counterparts exact. Private6retained original file/rawcontainer identities verified, explicitly not public review inputs. Transportchecker22valid0; missing/bytes/wrapper/zero-reference controls1; Pythoncompile0. Actual currentRR fulltip newdeclared row4 and prior3 remainvalid,2oldflatrefusals retained. Canonical portable reflection, fullsource/prefix/oldcontainer checks. No repeatRheos/implementation/compiler/package/backend/provider/service execution."
           :note "Simple own preparation reference gap found before publication, not product runtime fault. Original frozen9a9/history/metadata/fourcards/twonotes unchanged. Two resumed preparation mistakes (withheldURL terminator assertion and mkdir) retained/corrected; no originalsource/nativeeffects. No fabricated lossless unsanitized nativebody or public privateartifact availability."
           :decisions "Root sole publication after distinct frozenpeer/fresh nativeguard; initial Incoming13epic=existingreaction3+dedup5+watchlistpolicyshapes5 remains reviewproposed. Parent/current-head/nativeplanning/RheosReady holds; no providerrequest or paidsettings."}
           "octave-commons/bitch-tracker" now :adjudication)
        event (api/build-event {:event-id (str (random-uuid)) :recorded-at now
                 :component-manifest {:eta-mu/version "1.1.1"} :command "local full planning reference correction"
                 :producer {:actor "root/issues"} :subject {:repo "octave-commons/bitch-tracker"}} payload)
        line (edn/format-line event) result (api/validate-line line 1)]
   (when-not (:ok result) (throw (ex-info "Current owning API rejected receipt" (dissoc result :line :event))))
   (.appendFileSync fs target (str line "\n")) (prn (select-keys result [:ok :source/schema :errors])))
  (let [text (if (= mode "git") (.execFileSync child "git" #js ["show" (str target ":.ημ/receipts.edn")] #js {:encoding "utf8"}) (.readFileSync fs target "utf8"))
        lines (str/split-lines text)
        results (mapv (fn [i line] (select-keys (api/validate-line line (inc i)) [:ok :line-number :source/schema :errors])) (range) lines) own (last results)]
   (prn {:total-lines (count lines) :owned-addition own :historical-rows (dec (count lines)) :declared-suffix (vec (take-last 2 results)) :historical-refusals (vec (remove :ok (butlast results)))})
   (when-not (and (:ok own) (= :declared (get-in own [:source/schema :status]))) (set! (.-exitCode js/process) 1)))))
