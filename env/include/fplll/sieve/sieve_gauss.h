#ifndef FPLLL_SIEVE_GAUSS_H
#define FPLLL_SIEVE_GAUSS_H

#include "sieve_common.h"
#include "sieve_gauss_str.h"

using namespace std;
using namespace fplll;

FPLLL_BEGIN_NAMESPACE

/**
 * Gauss sieve
 */
template <class ZT, class F> class GaussSieve
{

public:
  GaussSieve(ZZ_mat<ZT> &B, int alg, bool ver, int seed);
  ~GaussSieve();

  void set_verbose(bool verbose);
  void set_target_norm2(Z_NR<ZT> norm);
  bool verbose;
  bool sieve(Z_NR<ZT> target_norm);

  /*
    void Init(const mat_ZZ& B, KleinSampler* sampler);
    bool Start();
  */
  int alg;

  /* norms/listsize for all iterations */
  vector<Z_NR<ZT>> iters_norm;
  vector<long> iters_ls;

  NumVect<Z_NR<ZT>> return_first();

private:
  int nr, nc;

  /* estimated list size */
  double mem_lower;
  ZZ_mat<ZT> b;

  Z_NR<ZT> best_sqr_norm;
  Z_NR<ZT> target_sqr_norm;

  /* statistics */
  long max_list_size;
  long samples;
  long iterations;
  long iterations_step;
  long collisions;
  long reductions;

  /* statistics for 2-, 3- and 4-red, set manually in init() */
  double mult;
  double add;
  F final_norm;

  /* List */
  list<ListPoint<ZT> *> List;

  /* Queue (recording vectors to be reduced) */
  queue<ListPoint<ZT> *> Queue;

  /* Queue (recording samples) */
  priority_queue<ListPoint<ZT> *> Queue_Samples;

  /* sampler */
  KleinSampler<ZT, F> *Sampler;

  /* list functions */
  void add_mat_list(ZZ_mat<ZT> &B);
  void init_list();
  void init_list_rand();
  void free_list_queue();
  void free_sampler();

  /* reduction functions */
  Z_NR<ZT> update_p_2reduce(ListPoint<ZT> *p);
  Z_NR<ZT> update_p_3reduce_2reduce(ListPoint<ZT> *p,
                                    typename list<ListPoint<ZT> *>::iterator &lp_it);
  Z_NR<ZT> update_p_3reduce(ListPoint<ZT> *p);
  Z_NR<ZT> update_p_4reduce_3reduce(ListPoint<ZT> *p);
  void update_p_4reduce_aux(ListPoint<ZT> *p, typename list<ListPoint<ZT> *>::iterator &lp_it);
  Z_NR<ZT> update_p_4reduce(ListPoint<ZT> *p);

  /* info functions */
  void print_curr_info();
  void print_final_info();

  bool run_2sieve();
  bool run_3sieve();
  bool run_4sieve();
};

FPLLL_END_NAMESPACE

#endif
