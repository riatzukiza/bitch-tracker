(ns bitch5-full-planning-receipt
 (:require [clojure.string :as str] [eta-mu.receipt-river.api :as api]
 [eta-mu.receipt-river.domain.receipt :as receipt] [eta-mu.receipt-river.shape.edn :as edn]
 ["node:fs" :as fs] ["node:child_process" :as child]))
(let [[mode target] *command-line-args*]
 (if (= mode "append")
  (let [now (.toISOString (js/Date.))
        payload (receipt/build-payload
          {:kind :decision :owner "root/issues" :origin "Codex isolated Bitch Tracker issue5 whole pure-law planning"
           :dod "Preserve existing Incoming P2 reaction three-point card/note and seven criteria; propose complete seven-concept/eight-invariant/seven-proof epic13 with reaction3 plus dedup5 plus watchlist-policy-shape5, no implementation or readiness"
           :pi "pr-sprint-planning+receipt-river" :host "independent-complete-persistent-worktree"
           :manifest "docs/agile/tasks/bt5-01-pure-reaction-label-state.md docs/agile/notes/reaction-label-law-plan.md docs/agile/tasks/bt5-full-pure-laws-epic.md docs/agile/tasks/bt5-02-supplied-time-dedup.md docs/agile/tasks/bt5-03-watchlist-policy-shapes.md docs/agile/notes/issue5-full-pure-laws-plan.md .ημ/verification/issue5-full-pure-law-planning .ημ/receipts.edn .ημ/session-mycology/ledger.md"
           :refs "issue:octave-commons/bitch-tracker5 parent:64af437938b15b0e0bd37c80cc01610a1dc25992 accepted:4f1015bae457e6b4890f80a5d312f4259fce3ddb RR:154440f3c997aa9208194bba59b5edbef3654f78 personalPR1-2"
           :tests "Canonical PR1 status FIRST success before full body/all seven files; source/workflow complete event surface read. Actual ef3 readonly network-unshared fixture read-task for four Incoming cards; no accepted config/gate/admission. Own initial title JSON-level checker failed after successful native read; retained and corrected to returned frontmatter. Exact inherited prefixes/identities/strict streams; actual current receipt builder/reader and canonical portable reflection. No implementation/compiler/package test/build/provider/Discord/Socket/shared-service execution."
           :note "Whole issue refinement and honest proposed decomposition, never reaction-only or TTL-only substitution. Original finite reaction metadata/history remain prefixes; body relation does not retroactively assign parent. New initial Markdown epic and two stories are review inputs; source code/workflows/events/config and external authority untouched. No old CodeRabbit completion transfer."
           :decisions "Review full equality/version/coercion/schema/TTL-range-capacity-order/threshold policy ABI, meaningful table/property/negative controls, actual JVM-CLJS identical fixtures, missing coverage/hosted test runner selection and full13 sizing. Parent/planning/current-head review and Rheos Ready remain holds; issues4/6 references not foreign UUID dependencies."}
           "octave-commons/bitch-tracker" now :decision)
        event (api/build-event {:event-id (str (random-uuid)) :recorded-at now
                 :component-manifest {:eta-mu/version "1.1.1"} :command "local whole issue5 planning refinement"
                 :producer {:actor "root/issues"} :subject {:repo "octave-commons/bitch-tracker"}} payload)
        line (edn/format-line event) result (api/validate-line line 1)]
   (when-not (:ok result) (throw (ex-info "Current owning API rejected receipt" (dissoc result :line :event))))
   (.appendFileSync fs target (str line "\n")) (prn (select-keys result [:ok :source/schema :errors])))
  (let [text (if (= mode "git") (.execFileSync child "git" #js ["show" (str target ":.ημ/receipts.edn")] #js {:encoding "utf8"}) (.readFileSync fs target "utf8"))
        lines (str/split-lines text)
        results (mapv (fn [i line] (select-keys (api/validate-line line (inc i)) [:ok :line-number :source/schema :errors])) (range) lines) own (last results)]
   (prn {:total-lines (count lines) :owned-addition own :historical-rows (dec (count lines)) :historical-refusals (vec (remove :ok (butlast results)))})
   (when-not (and (:ok own) (= :declared (get-in own [:source/schema :status]))) (set! (.-exitCode js/process) 1)))))
