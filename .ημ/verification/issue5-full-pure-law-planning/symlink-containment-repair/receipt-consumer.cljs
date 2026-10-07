(ns bitch3-symlink-repair-receipt
 (:require [clojure.string :as str] [eta-mu.receipt-river.api :as api]
 [eta-mu.receipt-river.domain.receipt :as receipt] [eta-mu.receipt-river.shape.edn :as edn]
 ["node:fs" :as fs] ["node:child_process" :as child]))
(let [[mode target] *command-line-args*]
 (if (= mode "append")
  (let [now (.toISOString (js/Date.))
        payload (receipt/build-payload
          {:kind :adjudication :owner "root/issues" :origin "Codex isolated BitchTracker3 transport symlink containment repair"
           :dod "Verify native P2 symlink escape; minimally resolve root/artifact containment/read validated path; preserve22positive/fournegative controls and wholeissue5 plan/history"
           :pi "pr-review-settlement+receipt-river" :host "new-independent-complete-persistent-repair-worktree"
           :manifest ".ημ/verification/issue5-full-pure-law-planning/reference-correction/verify-native-references.py .ημ/verification/issue5-full-pure-law-planning/symlink-containment-repair .ημ/receipts.edn .ημ/session-mycology/ledger.md"
           :refs "PR:riatzukiza/bitch-tracker3 parent:9c3ab3ea566f1002c4bfee7d16eb2e124ffc3375 base:64af437938b15b0e0bd37c80cc01610a1dc25992 review:5442714787 root:4207234458 thread:PRRT_kwDOU4Vc586p6oGF item:cr-comment:v1:7dbcf00263c2b4d7b508a6e0 RR:154440f3c997aa9208194bba59b5edbef3654f78"
           :tests "Canonical statusFIRST0 before fullreview. Unchanged baseline accepts harmless externalfile+intermediatedirectory symlinks0; after exact suggested repair both1. Eleven-case matrix: existing22positive0, fouroldnegative1, internalfile/directory/root-alias positives0, lexicaldotdot1; fictional external sentinel unchanged. Pythoncompile0; actualimmutablecurrentRR declared3/4/5 valid with2oldflatrefusals retained; canonicalportableSM. No provider/board/backend/application test suite or sharedservice execution."
           :note "Minimal evidence-adapter containment fix, no board semantics/second engine/TOCTOU overhaul. All prior captures/manifests/proofs and entire7concepts8invariants7proof/reaction7AC/Incoming/proposed13 unchanged. Private fictional repro establishes symlink escape, not realhost leakage/collision; safe review projections retain rawhash/privateprovenance."
           :decisions "Root sole publisher/settler after distinct peer; no providerrequest or paid/headlessCLI. Native approval/cohort/Ready remain separate; no historical rewrite or spore/liveevent."}
           "octave-commons/bitch-tracker" now :adjudication)
        event (api/build-event {:event-id (str (random-uuid)) :recorded-at now
                 :component-manifest {:eta-mu/version "1.1.1"} :command "local transport symlink containment repair"
                 :producer {:actor "root/issues"} :subject {:repo "octave-commons/bitch-tracker"}} payload)
        line (edn/format-line event) result (api/validate-line line 1)]
   (when-not (:ok result) (throw (ex-info "Current owning API rejected receipt" (dissoc result :line :event))))
   (.appendFileSync fs target (str line "\n")) (prn (select-keys result [:ok :source/schema :errors])))
  (let [text (if (= mode "git") (.execFileSync child "git" #js ["show" (str target ":.ημ/receipts.edn")] #js {:encoding "utf8"}) (.readFileSync fs target "utf8"))
        lines (str/split-lines text)
        results (mapv (fn [i line] (select-keys (api/validate-line line (inc i)) [:ok :line-number :source/schema :errors])) (range) lines) own (last results)]
   (prn {:total-lines (count lines) :owned-addition own :historical-rows (dec (count lines)) :declared-suffix (vec (take-last 3 results)) :historical-refusals (vec (remove :ok (butlast results)))})
   (when-not (and (:ok own) (= :declared (get-in own [:source/schema :status]))) (set! (.-exitCode js/process) 1)))))
