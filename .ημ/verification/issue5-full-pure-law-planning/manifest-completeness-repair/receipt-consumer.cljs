(ns bitch3-completeness-repair-receipt
 (:require [clojure.string :as str] [eta-mu.receipt-river.api :as api]
 [eta-mu.receipt-river.domain.receipt :as receipt] [eta-mu.receipt-river.shape.edn :as edn]
 ["node:fs" :as fs] ["node:child_process" :as child]))
(let [[mode target] *command-line-args*]
 (if (= mode "append")
  (let [now (.toISOString (js/Date.))
        payload (receipt/build-payload
          {:kind :adjudication :owner "root/issues" :origin "Codex isolated BitchTracker3 transport manifest completeness repair"
           :dod "Verify native P1 incomplete manifest set false positives; require all three manifests and exact22 manifest/path identities including duplicate/count/metadata refusal; retain resolved containment and whole issue5 plan/history"
           :pi "pr-review-settlement+receipt-river" :host "new-independent-complete-persistent-repair-worktree"
           :manifest ".ημ/verification/issue5-full-pure-law-planning/reference-correction/verify-native-references.py .ημ/verification/issue5-full-pure-law-planning/manifest-completeness-repair .ημ/receipts.edn .ημ/session-mycology/ledger.md"
           :refs "PR:riatzukiza/bitch-tracker3 parent:5bb822ebd871797ef789b68c42620a861e1da8cf base:64af437938b15b0e0bd37c80cc01610a1dc25992 review:5443573568 root:4207929993 thread:PRRT_kwDOU4Vc586p8WWL item:cr-comment:v1:b766ae10a69495b6e2adb4d9 RR:154440f3c997aa9208194bba59b5edbef3654f78"
           :tests "Canonical status FIRST exit0 before full review. Baseline falsely accepts missing manifest/six refs, omitted ref, equal-count replacement and duplicate22. Corrected23-case matrix passes with required manifest/identity/duplicate/metadata/JSON controls and all11 prior containment/control outcomes meaningfully retained in full22-reference fixtures. Python AST compile0. Actual immutable current RR declared3-6 valid with2old flat refusals retained; canonical portable SM. No provider/board/backend/application suite/sharedservice execution."
           :note "Minimal evidence-adapter completeness fix, existing containment hunk preserved; no board semantics/second engine/TOCTOU overhaul. All prior captures/manifests/proofs and entire7concepts8invariants7proof/reaction7AC/Incoming/proposed13 unchanged. Private controlled repro establishes incomplete-input false success, not realhost leakage/collision; safe review projections retain rawhash/privateprovenance."
           :decisions "Root sole publisher/settler after distinct peer; no providerrequest or paid/headlessCLI. Native approval/cohort/Ready remain separate; no historical rewrite or spore/liveevent."}
           "octave-commons/bitch-tracker" now :adjudication)
        event (api/build-event {:event-id (str (random-uuid)) :recorded-at now
                 :component-manifest {:eta-mu/version "1.1.1"} :command "local transport manifest completeness repair"
                 :producer {:actor "root/issues"} :subject {:repo "octave-commons/bitch-tracker"}} payload)
        line (edn/format-line event) result (api/validate-line line 1)]
   (when-not (:ok result) (throw (ex-info "Current owning API rejected receipt" (dissoc result :line :event))))
   (.appendFileSync fs target (str line "\n")) (prn (select-keys result [:ok :source/schema :errors])))
  (let [text (if (= mode "git") (.execFileSync child "git" #js ["show" (str target ":.ημ/receipts.edn")] #js {:encoding "utf8"}) (.readFileSync fs target "utf8"))
        lines (str/split-lines text)
        results (mapv (fn [i line] (select-keys (api/validate-line line (inc i)) [:ok :line-number :source/schema :errors])) (range) lines) own (last results)]
   (println (.stringify js/JSON (clj->js {:total-lines (count lines) :owned-addition own :historical-rows (dec (count lines)) :declared-suffix (vec (take-last 4 results)) :historical-refusals (vec (remove :ok (butlast results)))})))
   (when-not (and (:ok own) (= :declared (get-in own [:source/schema :status]))) (set! (.-exitCode js/process) 1)))))
