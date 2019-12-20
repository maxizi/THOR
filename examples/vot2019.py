from bench import run_bench


class DotDict(dict):
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, val):
        if key in self.__dict__:
            self.__dict__[key] = val
        else:
            self[key] = val


def load_eval_config():
    args = DotDict()
    args.dataset = 'VOT2018'
    args.tracker = 'SiamRPN'
    args.vanilla = True
    args.viz = False
    args.lb_type = 'ensemble'
    args.spec_video = ''
    args.save_path = 'Tracker'
    args.verbose = True

    return args


if __name__ == '__main__':
    
    # Evaluate tracker if results are already stored in results directory
    args = load_eval_config()
    run_bench(args_ext=args)